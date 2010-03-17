%define version	20070529
%define release	%mkrel 5

Name:      skkdic
Summary:   SKK Dictionaries for Japanese
Version:   %{version}
Release:   %{release}
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


