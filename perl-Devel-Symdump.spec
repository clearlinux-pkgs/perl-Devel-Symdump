#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-Symdump
Version  : 2.18
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/A/AN/ANDK/Devel-Symdump-2.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AN/ANDK/Devel-Symdump-2.18.tar.gz
Summary  : 'dump symbol names or the symbol table'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
Devel::Symdump - dump symbol names or the symbol table
SYNOPSIS
# Constructor
require Devel::Symdump;
@packs = qw(some_package another_package);
$obj = Devel::Symdump->new(@packs);        # no recursion
$obj = Devel::Symdump->rnew(@packs);       # with recursion

%package dev
Summary: dev components for the perl-Devel-Symdump package.
Group: Development
Provides: perl-Devel-Symdump-devel = %{version}-%{release}

%description dev
dev components for the perl-Devel-Symdump package.


%prep
%setup -q -n Devel-Symdump-2.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Devel/Symdump.pm
/usr/lib/perl5/vendor_perl/5.28.1/Devel/Symdump/Export.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::Symdump.3
