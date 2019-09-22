#!/bin/sh

currentPath=$(cd `dirname $0`; pwd);

sudo rm -rf /usr/local/bin/BMRenameFile;
sudo rm -rf /usr/local/etc/renamefile.py;

sudo cp $currentPath/source/BMRenameFile /usr/local/bin/BMRenameFile;
sudo chmod 777 /usr/local/bin/BMRenameFile;
sudo cp $currentPath/source/renamefile.py /usr/local/etc/renamefile.py;
sudo chmod 777 /usr/local/etc/renamefile.py;
