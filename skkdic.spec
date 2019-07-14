%define version	20070529
%define release	19

Name:      skkdic
Summary:   SKK Dictionaries for Japanese
Version:   %{version}
Release:	1
Group:     System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:   GPL
URL:       http://openlab.ring.gr.jp/skk/

# Use this file:
# http://openlab.jp/skk/skk/dic/SKK-JISYO.L 
Source0:   %{name}-%{version}.tar.bz2

BuildArch: noarch

%description
SKK dictionaries for Japanese.
SKK is a Simple Kana-to-Kanji conversion program.


%prep
%setup -q -n %name-%version.orig

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/skk
install -m 644 SKK-JISYO.* $RPM_BUILD_ROOT/%{_datadir}/skk

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_datadir}/skk/*




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 20070529-7mdv2011.0
+ Revision: 669982
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 20070529-6mdv2011.0
+ Revision: 607539
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 20070529-5mdv2010.1
+ Revision: 524078
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 20070529-4mdv2010.0
+ Revision: 427142
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 20070529-3mdv2009.1
+ Revision: 351519
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 20070529-2mdv2009.0
+ Revision: 225440
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20070529-1mdv2008.1
+ Revision: 127324
- kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 20070529-1mdv2008.0
+ Revision: 80099
- new release


* Sat Apr 29 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20060429-1mdk
- update SKK-JISYO.L

* Wed Nov 16 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20051112-1mdk
- update SKK-JISYO.L

* Tue Aug 09 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20050806-1mdk
- update SKK-JISYO.L

* Fri Feb 18 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20050212-1mdk
- new release

* Mon Dec 27 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20041227-1mdk
- first spec

