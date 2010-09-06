Summary: Utility for the creation of squashfs filesystems
Name: squashfs-tools
Version: 4.1
Release: 0.5.20100827%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://squashfs.sf.net
# cvs -d:pserver:anonymous@squashfs.cvs.sourceforge.net:/cvsroot/squashfs export -D 2010-08-27 squashfs
Source0: squashfs-4.1.tar.bz2
Patch0: squashfs-cflags.patch
Patch1: squashfs-xz.patch
# https://sourceforge.net/tracker/?func=detail&aid=3060400&group_id=63835&atid=505343
Patch2: squashfs-swap-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel
BuildRequires: xz-devel
BuildRequires: libattr-devel

%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains the utilities for manipulating squashfs filesystems.

%prep
%setup -q -n squashfs
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
pushd squashfs-tools
make RPM_OPT_FLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin $RPM_BUILD_ROOT/usr/sbin
install -m 755 squashfs-tools/mksquashfs $RPM_BUILD_ROOT/sbin/mksquashfs
install -m 755 squashfs-tools/unsquashfs $RPM_BUILD_ROOT%{_sbindir}/unsquashfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
/sbin/mksquashfs
%{_sbindir}/unsquashfs

%changelog
* Mon Sep 6 2010 Dan Horák <dan[at]danny.cz> - 4.1-0.5.20100827
- Add fixes for big-endian machines

* Sat Aug 28 2010 Bruno Wolff III <bruno@wolff.to> - 4.1-0.4.20100827
- Rebase to latest upstream.
- The main reason is to pick up a fix for large xattr similar to the large inode fix. This doesn't need to get backported as 4.0 doesn't have xattr support.
- An option was added to build without xattr support.
- Various source cleanups have been done as well.

* Tue Aug 03 2010 Bruno Wolff III <bruno@wolff.to> - 4.1-0.3.20100803
- Rebase to latest upstream
- Prevent warning message for xattr for virtual directory
- Fix issue with large inodes - BZ 619020

* Wed Jul 27 2010 Bruno Wolff III <bruno@wolff.to> - 4.1-0.2.20100727
- Rebase to latest upstream devel state. Mostly xattr fixes and cleanup.

* Wed Jun 08 2010 Bruno Wolff III <bruno@wolff.to> - 4.1-0.1.20100607
- Rebase to 4.1 prerelease with xz wrapper
- Provides lzma compression as an option.
- squashfs-fix-unsquashing-v3.patch is part of the 4.1 prerelease

* Wed May 5 2010 Kyle McMartin <kyle@redhat.com> 4.0-4
- squashfs-fix-unsquashing-v3.patch: pull in fix from cvs. Thanks pkl!
  (rhbz#523504)

* Thu Feb 18 2010 Kyle McMartin <kyle@redhat.com> 4.0-3
- Update to release tarball as opposed to cvs snapshot.
- Add dist tag.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 05 2009 Kyle McMartin <kyle@redhat.com> - 4.0-1
- Update to release 4.0

* Tue Mar 16 2009 Kyle McMartin <kyle@redhat.com> - 4.0-0.20090316
- update to cvs snap from 2009-03-16.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.20090126
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Kyle McMartin <kyle@redhat.com> - 4.0-0.20090125
- update to cvs snap that should unbreak big endian machines creating
  little endian fs.

* Mon Jan 12 2009  <katzj@redhat.com> - 4.0-0.20090112
- update to cvs snap that generates v4.0 images

* Tue Sep 30 2008 Jeremy Katz <katzj@redhat.com> - 3.4-1
- update to 3.4

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.3-2
- Autorebuild for GCC 4.3

* Fri Dec 14 2007 Jeremy Katz <katzj@redhat.com> - 3.3-1
- Update to 3.3

* Wed Sep  5 2007 Jeremy Katz <katzj@redhat.com> - 3.2-2
- fixes from package review (#226430)

* Tue Mar 20 2007 Jeremy Katz <katzj@redhat.com> - 3.2-1
- update to 3.2r2

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 3.0-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Jeremy Katz <katzj@redhat.com> - 3.0-3
- updated fragment size patch (#204638)

* Wed Aug 16 2006 Jeremy Katz <katzj@redhat.com> - 3.0-2
- add upstream patch for fragment size problem (#202663)

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

