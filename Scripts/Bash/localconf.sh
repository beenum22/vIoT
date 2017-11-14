#!/bin/bash
FILEPATH=/home/$USER/vIoT/Scripts/Bash/samples/local.conf
if [ $1 == "-h" ]; then
  echo "Usage: `basename $0` example cmd; ./localconf.sh rpi 192.168.0.101 192.168.0.100
       where
       -controller arguments (either leave the public ones or enter all the parameters)
           HOST_IP FLAT_INT PUB_INT FLOAT_NET PUB_GW FLOAT_RANGE
       -rpi
           HOST_IP SERVICE_HOST"
  exit 0
elif [ $1 == "controller" ]
then
    cp /home/$USER/vIoT/Scripts/Bash/samples/contLocal.conf $FILEPATH
    sed -i 's/#HOST_IP=/HOST_IP='$2'/' $FILEPATH
    sed -i 's/#FLAT_INTERFACE=/FLAT_INTERFACE='$3'/' $FILEPATH
    if [ $# -eq 7 ]
    then
        sed -i 's/#PUBLIC_INTERFACE=/PUBLIC_INTERFACE='$4'/' $FILEPATH
        sed -i 's~#FLOATING_RANGE=~FLOATING_RANGE='$5'~' $FILEPATH
        sed -i 's/#PUBLIC_NETWORK_GATEWAY=/PUBLIC_NETWORK_GATEWAY='$6'/' $FILEPATH
        IFS='-' read -ra floatRange <<< "$7"
        sed -i 's/#Q_FLOATING_ALLOCATION_POOL=start=,end=/Q_FLOATING_ALLOCATION_POOL=start='"${floatRange[0]}"',end='"${floatRange[1]}"'/' $FILEPATH
    fi
elif [ $1 == "compute" ]
then
    cp /home/$USER/vIoT/Scripts/Bash/samples/rpiLocal.conf $FILEPATH 
    sed -i 's/#HOST_IP=/HOST_IP='$2'/' $FILEPATH
    sed -i 's/#SERVICE_HOST=/SERVICE_HOST='$3'/' $FILEPATH
fi

exit 0
