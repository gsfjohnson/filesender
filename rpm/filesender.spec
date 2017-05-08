#
# Also the Source0 URL will be adapted by the builder-scripts when needed
#

%define realname filesender

Name:           filesender16
Version:        1.6.1
Release:        1%{?dist}
Summary:        Sharing large files with a browser

Group:          Applications/Internet
License:        BSD
URL:            http://www.filesender.org/
Source0:        http://repository.filesender.org/releases/%{realname}-%{version}.tar.bz2
Source2:        %{realname}.htaccess
Source3:        %{realname}.cron.daily
BuildRoot:      %{_tmppath}/%{realname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires: httpd
Requires: php >= 5.2.0
Requires: php-xml
Requires: simplesamlphp
Requires: postgresql-server
Requires: php-pgsql

%description
FileSender is a web based application that allows authenticated users to
securely and easily send arbitrarily large files to other users.
Authentication of users is provided through SAML2, LDAP and RADIUS.
Users without an account can be sent an upload voucher by an
authenticated user. FileSender is developed to the requirements of the
higher education and research community.
.
The purpose of the software is to send a large file to someone, have
that file available for download for a certain number of downloads and/or
a certain amount of time, and after that automatically delete the file.
The software is not intended as a permanent file publishing platform.


%prep
%setup -q -n %{realname}-%{version}

%build

%install
rm -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_datadir}/%{realname}
%{__mkdir} -p %{buildroot}%{_sysconfdir}/%{realname}
%{__mkdir} -p %{buildroot}%{_sysconfdir}/httpd/conf.d
%{__mkdir} -p %{buildroot}%{_sysconfdir}/cron.daily
%{__mkdir} -p %{buildroot}%{_sysconfdir}/php.d
%{__mkdir} -p %{buildroot}%{_localstatedir}/lib/%{realname}/files
%{__mkdir} -p %{buildroot}%{_localstatedir}/lib/%{realname}/tmp
%{__mkdir} -p %{buildroot}%{_localstatedir}/log/%{realname}

%{__cp} -ad ./*       %{buildroot}%{_datadir}/%{realname}
%{__cp} -p %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{realname}.conf
%{__cp} -p %{SOURCE3} %{buildroot}%{_sysconfdir}/cron.daily/%{realname}

%{__cp} -p config-templates/filesender-php.ini                %{buildroot}%{_sysconfdir}/php.d/%{realname}.ini
%{__cp} -p config/config-dist.php                             %{buildroot}%{_sysconfdir}/%{realname}/config-dist.php
%{__cp} -p %{buildroot}%{_sysconfdir}/%{realname}/config-dist.php %{buildroot}%{_sysconfdir}/%{realname}/config.php

%{__rm} -f %{buildroot}%{_datadir}/%{realname}/*.txt
%{__rm} -f %{buildroot}%{_datadir}/%{realname}/*.specs

%{__rm} -rf %{buildroot}%{_datadir}/%{realname}/config
%{__rm} -rf %{buildroot}%{_datadir}/%{realname}/tmp
%{__rm} -rf %{buildroot}%{_datadir}/%{realname}/log
%{__rm} -rf %{buildroot}%{_datadir}/%{realname}/files

ln -s %{_sysconfdir}/%{realname}              %{buildroot}%{_datadir}/%{realname}/config
ln -s %{_localstatedir}/lib/%{realname}/tmp   %{buildroot}%{_datadir}/%{realname}/tmp
ln -s %{_localstatedir}/lib/%{realname}/files %{buildroot}%{_datadir}/%{realname}/files
ln -s %{_localstatedir}/log/%{realname}       %{buildroot}%{_datadir}/%{realname}/log

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.txt INSTALL.txt LICENCE.txt README.txt
%{_datadir}/%{realname}/
%dir %{_sysconfdir}/%{realname}/
%attr(0640,root,apache) %{_sysconfdir}/%{realname}/config-dist.php
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/%{realname}/config.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{realname}.conf
%config(noreplace) %{_sysconfdir}/php.d/%{realname}.ini
%config(noreplace) %attr(0755,root,root) %{_sysconfdir}/cron.daily/%{realname}
%dir %{_localstatedir}/lib/%{realname}/
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{realname}/tmp
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{realname}/files
%dir %attr(0750,apache,apache) %{_localstatedir}/log/%{realname}


%changelog
* Sun May 07 2017 FileSender Development <filesender-dev@filesender.org> 1.6.1-1
- Release 1.6.1

* Sun Mar 03 2013 FileSender Development <filesender-dev@filesender.org> 1.5-1
- Release 1.5

* Mon Oct 22 2012 FileSender Development <filesender-dev@filesender.org> 1.5-0.7.rc1
- Release 1.5-rc1

* Wed Jul 25 2012 FileSender Development <filesender-dev@filesender.org> 1.5-0.6.beta4
- Release 1.5-beta4

* Tue May 15 2012 FileSender Development <filesender-dev@filesender.org> 1.5-0.5.beta3
- Release 1.5-beta3

* Wed Apr 25 2012 FileSender Development <filesender-dev@filesender.org> 1.5-0.4.beta2
- Release 1.5-beta2

* Mon Feb 13 2012 FileSender Development <filesender-dev@filesender.org> 1.5-0.1.beta1
- Release 1.5-beta1

* Sat Nov 05 2011 FileSender Development <filesender-dev@filesender.org> 1.1-1
- Release 1.1

* Wed May 11 2011 FileSender Development <filesender-dev@filesender.org> 1.0.1-1
- Release 1.0.1

* Mon Jan 31 2011 FileSender Development <filesender-dev@filesender.org> 1.0-1
- Release 1.0