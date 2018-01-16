Name:		hpc-config
Version:	1.1.6
Release:	1%{?dist}
License:	GPLv2+
Summary:	Suite of utilities to deploy HPC clusters generic configuration
URL:		https://github.com/edf-hpc/hpc-config
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
hpc-config is a suite of utilities to ease deployment of Puppet-HPC, a
Puppet-based software stack designed to easily deploy HPC clusters. The main
goal of Puppet-HPC is to provide a common generic configuration management
system that can be used effortlessly across multiple HPC clusters and
organizations.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -m 755 -d $RPM_BUILD_ROOT/%{_sbindir}
install -m 755 scripts/hpc-config-apply $RPM_BUILD_ROOT/%{_sbindir}/hpc-config-apply
install -m 755 -d $RPM_BUILD_ROOT/%{_initddir}
install -m 755 init/el6/hpc-config-apply $RPM_BUILD_ROOT/%{_initddir}/hpc-config-apply

%clean
rm -rf %{buildroot}

%package apply
Summary: %{name}-apply script to deploy the configuration on a node
Requires: python34, python34-PyYAML, python34-urllib3

%description apply
This package provides the tool necessary to deploy the configuration
on a RHEL node. It also provide a service file that applies it during
the boot sequence.

%files apply
%defattr(-,root,root,-)
%doc README.md
%{_sbindir}/hpc-config-apply
%{_initddir}/hpc-config-apply

%changelog

* Tue Jan 16 2018 Thomas Hamel <thomas-externe.hamel@edf.fr> - 1.1.6
  - New release 1.1.6
  - Optimize hpc-config-push

* Thu Aug 17 2017 Thomas Hamel <thomas-externe.hamel@edf.fr> - 1.1.4
  - New release 1.1.4

* Tue Aug 08 2017 Thomas Hamel <thomas-externe.hamel@edf.fr> - 1.1.3
  - New release 1.1.3

* Tue Aug 08 2017 Thomas Hamel <thomas-externe.hamel@edf.fr> - 1.1.2
  - New release 1.1.2

* Tue May 30 2017 Thomas Hamel <thomas-externe.hamel@edf.fr> - 1.1.0
  - Initial release 1.1.0
