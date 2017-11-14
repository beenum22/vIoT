#!/bin/bash
stackDir=/opt/stack
#workDir=$HOME/vIoT
workDir=..
IFS=' ' read -r -a repos <<< "$1"
echo "Cloning devstack."
if [ $2 == 'custom' ]; then
    git clone https://github.com/beenum22/devstack $workDir/devstack
else
    git clone https://github.com/openstack-dev/devstack $workDir/devstack
fi
#git clone https://github.com/beenum22/devstack $workDir/devstack
echo "Copying local.conf to '$workDir'/devstack"
cp $workDir/Scripts/Bash/samples/local.conf $workDir/devstack/
if [ -d "$stackDir" ]
then
    echo "Directory '$stackDir' Exists"
else
    echo "Error: Directory '$stackDir' does not exists."
    sudo mkdir $stackDir
    echo "$stack Created"
    echo "Changing owner of '$stackDir' to '$USER'"
    sudo chown -R $USER $stackDir
fi
if [ $2 == 'custom']
then
    for r in "${repos[@]}";do
        if [ -d "$stackDir/$r" ]; then
            echo "Directory $r already exists"
        else
            echo "Cloning $r"
            git clone https://github.com/beenum22/$r $stackDir/$r
        fi
    done
fi
echo "It's time to run start Devstack."
cd $workDir/devstack && ./stack.sh

# Run script/s for images, flavors and zones

exit 0

