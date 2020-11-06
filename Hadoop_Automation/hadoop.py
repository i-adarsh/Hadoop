import os

def configureHadoop(choice):
    if choice == "1":
        os.system("yum install wget -y")
        os.system("wget http://83.103.170.157/apps/java/jdk_1.8/jdk/jdk-8u202-linux-x64.rpm")
        os.system("rpm -ivh jdk-8u202-linux-x64.rpm")
        os.system("wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
        os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
        os.system("rm -rf /etc/hadoop/core-site.xml")
        os.system("rm -rf /etc/hadoop/hdfs-site.xml")
        dataNode = open("hdfs-site.xml", "w+")
        infile = open("hdfs.xml", "r+")
        for line in infile:
            if line == "<value>/nameNode</value>" or line == "<value>/dataNode</value>":
                line = "<value>/nameNode</value>"
            dataNode.write(line)
        dataNode.close()
        infile.close()
        dataNode = open("core-site.xml", "w+")
        ip = "0.0.0.0"
        infile = open("core.xml", "r+")
        i = 1
        for line in infile:
            i += 1
            if i == 10:
                line = "<value>hdfs://" + ip + ":9001</value>\n"
            dataNode.write(line)
        infile.close()
        dataNode.close()
        os.system("cp -f core-site.xml /etc/hadoop/")
        os.system("cp -f hdfs-site.xml /etc/hadoop/")
        os.system("systemctl stop firewalld")
        os.system("hadoop namenode -format -y")
        os.system("hadoop-daemon.sh start namenode")
        os.system("netstat -tnlp")

    if choice == "2":
        os.system("yum install wget -y")
        os.system("wget http://83.103.170.157/apps/java/jdk_1.8/jdk/jdk-8u202-linux-x64.rpm")
        os.system("rpm -ivh jdk-8u202-linux-x64.rpm")
        os.system("wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
        os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
        os.system("rm -rf /etc/hadoop/core-site.xml")
        os.system("rm -rf /etc/hadoop/hdfs-site.xml")
        dataNode = open("hdfs-site.xml", "w+")
        infile = open("hdfs.xml", "r+")
        number = input("Enter Number of dataNode : ")
        for line in infile:
            if line == "<property>\n" or line == "</property>\n":
                line = "\n"
            if line == "<value>/nameNode</value>\n":
                line = "<value>/dataNode" + number + "</value>\n"
            dataNode.write(line)
        dataNode.close()
        infile.close()
        dataNode = open("core-site.xml", "w+")
        ip = input("Enter Ip of the Master Node : ")
        infile = open("core.xml", "r+")
        i = 1
        for line in infile:
            i += 1
            if i == 10:
                line = "<value>hdfs://" + ip + ":9001</value>\n"
            print(line)
            dataNode.write(line)
        infile.close()
        dataNode.close()
        os.system("cp -f core-site.xml /etc/hadoop/")
        os.system("cp -f hdfs-site.xml /etc/hadoop/")
        os.system("systemctl stop firewalld")
        os.system("hadoop-daemon.sh start datanode")
        os.system("netstat -tnlp")
        
        
choice = input('''Setup Hadoop

1. Configure NameNode
2. Configure DataNode

Enter Your choice : ''')
configureHadoop(choice)
