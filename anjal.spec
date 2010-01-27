Name: anjal
Version: 0.3.1
Release: %mkrel 1
Summary: An email client for small screen devices
Group: Applications/Productivity
License: LGPLv2 or LGPLv3
URL: http://live.gnome.org/Anjal/
Source0: ftp://ftp.gnome.org/pub/gnome/sources/%{name}/0.3/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: evolution-devel
BuildRequires: evolution-data-server-devel
BuildRequires: libGConf2-devel
BuildRequires: libglade2-devel
BuildRequires: gtk2-devel
BuildRequires: webkitgtk-devel
BuildRequires: unique-devel
BuildRequires: sqlite3-devel
BuildRequires: libxml2-devel
BuildRequires: intltool

%description
Anjal is a mail client for small screen devices like NetBooks. It 
features a nice multi-line message list, with text-preview of the 
latest messages in the thread. It supports a tab interface for 
folders, new mail and config. Being based on evolution it supports 
all the mail backends including POP3, IMAP4, Exchange and GroupWare.

%prep
%setup -q

%build
%configure2_5x --disable-static --with-mozilla=no --with-anerley=no --disable-schemas-install
%make

%install
rm -rf %{buildroot}
%makeinstall_std

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%find_lang %{name}

%preun
%preun_uninstall_gconf_schemas %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING TODO README
%{_sysconfdir}/gconf/schemas/anjal.schemas
%{_bindir}/anjal
%{_bindir}/anjal-settings
%{_datadir}/anjal
%{_datadir}/applications/anjal.desktop
%{_datadir}/applications/anjal-settings.desktop
%{_datadir}/gnome-control-center/default-apps/anjal.xml
%{_libdir}/evolution/*/anjal/libeshell-module-anjal.so
