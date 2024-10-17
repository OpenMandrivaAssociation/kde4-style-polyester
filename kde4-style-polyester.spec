%define base_name	kde4-style
%define theme_name	polyester
%define name		%base_name-%theme_name
%define version		2.0.0
%define rel             2
%define release		%mkrel %rel
%define summary		Polyester kde widget style for KDE4

Name:			%name
Version:		%version
Release:		%release
Summary:		%summary
License:		LGPL
Group:			Graphical desktop/KDE
Source:			http://www.notmart.org/files/polyester-%version.tar.bz2
URL:			https://kde-look.org/content/show.php?content=27968
Requires:		kdelibs4-core
BuildRequires:		kdebase4-workspace-devel
BuildRoot:		%_tmppath/%name-buildroot

%description
Polyester is a kde widget style aimed to be a good balance between eye candy
and simplicity.

%prep
%setup -q -n %theme_name-%version

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build 

%find_lang kstyle_%{theme_name}_config

%clean
rm -rf %buildroot

%files -f kstyle_%{theme_name}_config.lang
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING README 
%_kde_libdir/kde4/libpolyester_config.so
%_kde_libdir/kde4/plugins/styles/libpolyester.so
%_kde_datadir/apps/color-schemes/Polyester*.colors
%_kde_datadir/apps/kstyle/themes/polyester.themerc



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdv2011.0
+ Revision: 619946
- the mass rebuild of 2010.0 packages

* Sun May 03 2009 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 370819
- fix tarball dir
- 2.0.0

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 2.0-0.beta2.1mdv2009.1
+ Revision: 336439
- 1.98.0

* Fri Jul 04 2008 Funda Wang <fwang@mandriva.org> 2.0-0.beta1.2mdv2009.0
+ Revision: 231545
- rebuild

* Thu May 15 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 2.0-0.beta1.1mdv2009.0
+ Revision: 207611
- import kde4-style-polyester


