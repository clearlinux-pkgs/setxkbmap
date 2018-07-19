#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setxkbmap
Version  : 1.3.1
Release  : 1
URL      : https://www.x.org/releases/individual/app/setxkbmap-1.3.1.tar.bz2
Source0  : https://www.x.org/releases/individual/app/setxkbmap-1.3.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : HPND
Requires: setxkbmap-bin
Requires: setxkbmap-license
Requires: setxkbmap-man
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xorg-macros)

%description
setxkbmap is an X11 client to change the keymaps in the X server for a
specified keyboard to use the layout determined by the options listed
on the command line.

%package bin
Summary: bin components for the setxkbmap package.
Group: Binaries
Requires: setxkbmap-license
Requires: setxkbmap-man

%description bin
bin components for the setxkbmap package.


%package license
Summary: license components for the setxkbmap package.
Group: Default

%description license
license components for the setxkbmap package.


%package man
Summary: man components for the setxkbmap package.
Group: Default

%description man
man components for the setxkbmap package.


%prep
%setup -q -n setxkbmap-1.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531976975
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1531976975
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/setxkbmap
cp COPYING %{buildroot}/usr/share/doc/setxkbmap/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/setxkbmap

%files license
%defattr(-,root,root,-)
/usr/share/doc/setxkbmap/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/setxkbmap.1
