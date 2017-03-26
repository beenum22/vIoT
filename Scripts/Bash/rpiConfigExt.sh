#!/bin/bash

workDir=$HOME/vIoT
echo "Resizing the filesystem."
sudo mkdir /mnt/fat16 && sudo mkdir /mnt/ext4
echo -e 'unit chs\nrm 2\nmkpart primary '$2' 1950,251,28\nquit' | sudo parted /dev/$1
sudo e2fsck -f /dev/$12
sudo resize2fs /dev/$12
echo "Successfully resized the filesystem."
echo "Adding custom kernel..."
KERNEL=kernel7
sudo mount /dev/$11 /mnt/fat16 && sudo mount /dev/$12 /mnt/ext4
sudo cp -R $workDir/Kernel/lib/* /mnt/ext4/lib/
sudo cp /mnt/fat16/$KERNEL.img /mnt/fat16/$KERNEL-backup.img
sudo cp $workDir/Kernel/$KERNEL.img /mnt/fat16/
sudo cp $workDir/Kernel/*.dtb /mnt/fat16/
sudo cp $workDir/Kernel/overlays/*.dtb* /mnt/fat16/overlays/
sudo cp $workDir/Kernel/overlays/README /mnt/fat16/overlays/
echo "Successfully installed custom kernel."
sudo sed -i 's/^PermitRootLogin.*/PermitRootLogin without-password/' /mnt/ext4/etc/ssh/sshd_config
echo "Passwordless ssh to the compute node root enabled."
mkdir /mnt/ext4/home/ubuntu/.ssh && sudo mkdir /mnt/ext4/root/.ssh && /mnt/ext4/home/ubuntu/vIoT
touch /mnt/ext4/home/ubuntu/.ssh/authorized_keys
sudo touch /mnt/ext4/root/.ssh/authorized_keys
sudo cat ~/.ssh/id_rsa.pub >> /mnt/ext4/home/ubuntu/.ssh/authorized_keys
sudo cat ~/.ssh/id_rsa.pub >> /mnt/ext4/root/.ssh/authorized_keys
echo "Controller's public key added to the compute node for remote access."
echo "Adding vIoT codebase to compute node."
sudo cp ~/vIoT/Scripts.tar.xz /mnt/ext4/home/ubuntu/vIoT/
sudo umount /mnt/fat16
sudo umount /mnt/ext4

exit 0