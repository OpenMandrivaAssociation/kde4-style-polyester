%define base_name	kde4-style
%define theme_name	polyester
%define name		%base_name-%theme_name
%define version		2.0.0
%define rel             1
%define release		%mkrel %rel
%define summary		Polyester kde widget style for KDE4

Name:			%name
Version:		%version
Release:		%release
Summary:		%summary
License:		LGPL
Group:			Graphical desktop/KDE
Source:			http://www.notmart.org/files/polyester-%version.tar.bz2
URL:			http://kde-look.org/content/show.php?content=27968
Requires:		kdelibs4-core
BuildRequires:		kdebase4-workspace-devel
BuildRoot:		%_tmppath/%name-buildroot

%description
Polyester is a kde widget style aimed to be a good balance between eye candy
and simplicity.

%prep
%setup -q -n %theme_name-1.98.0

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

