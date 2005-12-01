Summary: squashfs utilities
Name: squashfs-tools
Version: 2.2r2
Release: 1
License: GPL
Group: System Environment/Base
URL: http://squashfs.sf.net
Source0: squashfs2.2-r2.tar.gz
Patch0: squashfs-cflags.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains the utilities for manipulating squashfs filesystems.

%prep
%setup -q -n squashfs2.2-r2
%patch0 -p1

%build
pushd squashfs-tools
make RPM_OPT_FLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
install -m 755 squashfs-tools/mksquashfs $RPM_BUILD_ROOT/sbin/mksquashfs

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README PERFORMANCE.README COPYING ACKNOWLEDGEMENTS CHANGES
/sbin/mksquashfs

%changelog
* Thu Dec  1 2005 Jeremy Katz <katzj@redhat.com> - 2.2r2-1
- Initial build

