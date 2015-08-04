Name:           kibana
Version:        4.1.1
Release:        1%{?dist}
Summary:        Open source data visualization platform

License:        Apache v2
URL:            https://www.elastic.co/products/kibana 
Source0:        https://download.elastic.co/kibana/kibana/kibana-4.1.1-linux-x64.tar.gz
Source1:	https://github.com/usualstuff/kibana-rpm

%description
Kibana is an open source data visualization platform that allows you to interact with your data through stunning, powerful graphics that can be combined into custom dashboards that help you share insights from your data far and wide. 

%prep
#copying files from source1 to build dir
cp ../SOURCES/kibana-rpm/{kibana,kibana.service} .
%setup -n kibana-4.1.1-linux-x64

%define debug_package %{nil}


%build
%install
rm -rf $RPM_BUILD_ROOT

#making dirs
mkdir -p $RPM_BUILD_ROOT/etc/kibana
mkdir -p $RPM_BUILD_ROOT/opt/kibana
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/

#installing files from source0
cp -r {node,src} $RPM_BUILD_ROOT/opt/kibana
cp config/kibana.yml $RPM_BUILD_ROOT/etc/kibana

#installing files from source1
cp ../kibana.service $RPM_BUILD_ROOT/usr/lib/systemd/system/kibana.service
cp ../kibana $RPM_BUILD_ROOT/etc/sysconfig/kibana

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf ../systemd

%files
%defattr(-,root,root,-)
%config /etc/sysconfig/kibana
/usr/lib/systemd/system/kibana.service
%config /etc/kibana/kibana.yml
/opt/kibana/*

%changelog
