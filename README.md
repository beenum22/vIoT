# vIoT
A First Step Towards a Shared, Multi-tenant IoT Infrastructure Architecture

## vIoT Automation
This project's main goal is to make the vIoT deployment and testing faster and easy. It consists of different directories named accordingly such as;
* Images
* Kernel
* Scripts
* BackUp
### Images
This directory consists of all the required images used during and after the deployment
### Kernel
On ARM architecture, kernel needs to be modified and some extra modules are enabled so LXD can work on it. This directory consists of an already compiled kernel.
### Scripts
This directory consists of two python codes basically, one for the deployment while the other for testing purposes such as calculating time delays etc.
#### Automated Deployment
Run `python automation.py -h`
### Automated Tests
Run `python containersTime.py -h`

## Abstract
This paper describes a virtualized Internet of Things (vIoT) testbed. We argue in favor of an IoT Infrastructure-as-a-Service as a possible deployment model for future IoTs. The vIoT testbed is being built from open source components, most notably comprising of OpenStack, Linux containers and Raspberry Pi computers. Results demonstrates vIoT infrastructure configured to be shared by multiple users using with LXC/LXD running containers of Ubuntu Trusty Tahr, Ubuntu Xenial Xerus and CirrOS.

## Testbed Architecture
The vIoT testbed comprises of three principal components, shown in Figure 5; The OpenStack CMS, Raspberry Pi 2 Model B IoT devices and LXD Linux containers. The Raspberry Pi 2 layer comprises of the fog layer of our vIoT testbed, which lies between sensors and the cloud data center. The native OS installed on the Raspberry Pi 2s is Ubuntu 15.10 Wily Werewolf with MATE 1.10.0 and Linux kernel 4.4.0-22-generic. Since none of the hypervisors supported for the ARM v7 used in the Raspberry Pi 2 Model B are supported by OpenStack, we use LXC / LXD for virtualization technology. Each IoT application’s component executing in the fog layer is run on LXC containers managed by LXD, which is integrated into our OpenStack-based private cloud using the nova-lxd plugin. Users can deploy their applications with complete isolation from what other tenants may be doing and manage them through OpenStack’s Horizon dashboard.

## Conclusion
The IoT’s rapid growth is fostering the development of novel, heretofore unseen applications. The need for a fully shareable virtualized IoT has received very limited attention to-date, but there is an ever-growing set of use-cases that can benefit from having the capability to allow users to reserve virtual resources on IoT devices. In this paper, we have described the vIoT testbed currently under development that will serve as a prototype / proof-of-concept for the IoT-IaaS. We described the significant architectural components of the vIoT testbed. In essence, the vIoT testbed extends the deployment of OpenStack all the way to the IoT devices in the manner described as fog computing. We are using Raspberry Pi 2 Model B computers as stand-ins for IoT devices and are deploying Linux containers on them. The vIoT testbed will also have to extend the sharing of resources to the sensors attached to IoT devices.
