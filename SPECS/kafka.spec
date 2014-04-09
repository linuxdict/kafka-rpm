%define __jar_repack 0
Summary: Kafka and distributed topic based producer consumer queue
Name: kafka
Version: 0.8.0
Release: 1
License: Apache (v2)
Group: Applications
Source0: %{name}-%{version}-src.tgz
Source1: ftp://ftp.nowhere.com/kafka.init
Source2: ftp://ftp.nowhere.com/kafka-zookeeper.init
URL: http://kafka.apache.org
#BuildRoot: tmp/kafka-0.7.1
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Distribution: huffpo
Vendor: huffpo
Packager: edlinuxguru@gmail.com

#I rarely have a packaged java
#Prereq: jdk >= 1.6

%description
Follow this example and you can do no wrong

%prep

%setup -q -n %{name}-%{version}-src

%build
./sbt update
./sbt package
./sbt release-zip

%install
pwd
mkdir -p $RPM_BUILD_ROOT/opt/kafka
mkdir -p $RPM_BUILD_ROOT/opt/kafka/config

#../tmp/kafka-0.8.0-src/target/RELEASE/kafka_2.8.0-0.8.0/
cp -r target/RELEASE/kafka_2.8.0-0.8.0/bin $RPM_BUILD_ROOT/opt/kafka

cp -r target/RELEASE/kafka_2.8.0-0.8.0/config $RPM_BUILD_ROOT/opt/kafka/config-sample

cp -r target/RELEASE/kafka_2.8.0-0.8.0/libs $RPM_BUILD_ROOT/opt/kafka/libs

cp -r target/RELEASE/kafka_2.8.0-0.8.0/kafka_2.8.0-0.8.0.jar $RPM_BUILD_ROOT/opt/kafka

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install  -m 755 %{S:1} $RPM_BUILD_ROOT/etc/rc.d/init.d/kafka
install  -m 755 %{S:2} $RPM_BUILD_ROOT/etc/rc.d/init.d/kafka-zookeeper

%files
%defattr(-,root,root)

%config %attr(755,root,root) /opt/kafka/config

/opt/kafka
/etc/rc.d/init.d/kafka
/etc/rc.d/init.d/kafka-zookeeper

%clean
#used to cleanup things outside the build area and possibly inside.

%changelog
* Wed Apr 9 2014 Edward Capriolo <edlinuxguru@gmail.com>
- Update to Kafka 0.8.0 encorporate some changes from https://github.com/kosii/kafka-rpm/
* Wed Jul 11 2012 Edward Capriolo <edward@m6d.com>
- Rebuild against kafka trunk for mirror mode support
* Mon May  7 2012  Edward Capriolo <edward@m6d.com>
- Fix init scripts, clear conf dir, skip system test dir
* Tue May  3 2012  Edward Capriolo <edward@m6d.com>
- Taking care of business
* Tue May  2 2012  Edward Capriolo <edward@m6d.com>
- Oldest at the bottom 

