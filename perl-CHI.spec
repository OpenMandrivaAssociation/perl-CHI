%define upstream_name    CHI
%define upstream_version 0.55

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Nothing is cached
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp::Assert)
BuildRequires:	perl(Data::UUID)
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl(Digest::JHash)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Hash::MoreUtils)
BuildRequires:	perl(JSON)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Log::Any)
BuildRequires:	perl(Log::Any::Adapter)
BuildRequires:	perl-Log-Any-Adapter
BuildRequires:	perl(Log::Any::Adapter::Dispatch)
BuildRequires:	perl(Module::Load::Conditional)
BuildRequires:	perl(Moose)
BuildRequires:	perl(String::RewritePrefix)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Class)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Log::Dispatch)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Time::Duration)
BuildRequires:	perl(Time::Duration::Parse)
BuildArch:	noarch

%description
CHI provides a unified caching API, designed to assist a developer in
persisting data for a specified period of time.

The CHI interface is implemented by driver classes that support fetching,
storing and clearing of data. Driver classes exist or will exist for the
gamut of storage backends available to Perl, such as memory, plain files,
memory mapped files, memcached, and DBI.

CHI is intended as an evolution of DeWitt Clinton's Cache::Cache package,
adhering to the basic Cache API but adding new features and addressing
limitations in the Cache::Cache implementation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.360.0-4mdv2011.0
+ Revision: 654239
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.360.0-3mdv2011.0
+ Revision: 625064
- Trying to fix the deps
- Add a missing build requires
- import perl-CHI

