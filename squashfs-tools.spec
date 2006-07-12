Summary: squashfs utilities
Name: squashfs-tools
Version: 3.0
Release: 1.1
License: GPL
Group: System Environment/Base
URL: http://squashfs.sf.net
Source0: squashfs3.0.tar.gz
Patch0: squashfs-cflags.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel

%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains the utilities for manipulating squashfs filesystems.

%prep
%setup -q -n squashfs3.0
%patch0 -p1 -b .cflags

%build
pushd squashfs-tools
make RPM_OPT_FLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin $RPM_BUILD_ROOT/usr/sbin
install -m 755 squashfs-tools/mksquashfs $RPM_BUILD_ROOT/sbin/mksquashfs
install -m 755 squashfs-tools/unsquashfs $RPM_BUILD_ROOT/usr/sbin/unsquashfs

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README PERFORMANCE.README COPYING ACKNOWLEDGEMENTS CHANGES
/sbin/mksquashfs
/usr/sbin/unsquashfs

%changelog
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.0-1.1
- rebuild

* Fri Jun 23 2006 Jeremy Katz <katzj@redhat.com> - 3.0-1
- update to 3.0
- include unsquashfs

* Tue May 16 2006 Jeremy Katz <katzj@redhat.com> 
- add BR on zlib-devel (Andreas Thienemann, #191880)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.2r2-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.2r2-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  1 2005 Jeremy Katz <katzj@redhat.com> - 2.2r2-1
- Initial build

