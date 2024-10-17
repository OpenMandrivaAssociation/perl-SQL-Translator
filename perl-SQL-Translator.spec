%define upstream_name	 SQL-Translator
%define upstream_version 0.11018

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Doesnt(.*)\\)|perl\\(GD(.*)\\)|perl\\(GraphViz(.*)\\)|perl\\(IO::File(.*)\\)|perl\\(IO::Scalar(.*)\\)|perl\\(Spreadsheet::ParseExcel(.*)\\)|perl\\(Template(.*)\\)|perl\\(Text::ParseWords(.*)\\)|perl\\(Text::RecordParser(.*)\\)|perl\\(XML::Writer(.*)\\)|perl\\(XML::XPath(.*)\\)'
%else
%define _requires_exceptions perl(Doesnt\\|perl(GD\\|perl(GraphViz\\|perl(IO::File\\|perl(IO::Scalar\\|perl(Spreadsheet::ParseExcel\\|perl(Template\\|perl(Text::ParseWords\\|perl(Text::RecordParser\\|perl(XML::Writer\\|perl(XML::XPath
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Manipulate structured data definitions (SQL and more)
License:	GPL
Group:		Development/Perl
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/SQL/SQL-Translator-%{upstream_version}.tar.gz
Url:		https://search.cpan.org/dist/%{upstream_name}

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Base)
BuildRequires:	perl(Class::Data::Inheritable) >= 0.02
BuildRequires:	perl(Class::MakeMethods)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(IO::Dir)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Log::Log4perl)
BuildRequires:	perl(Moo)
BuildRequires:	perl(Parse::RecDescent) >= 1.94
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More) >= 0.6
BuildRequires:	perl(XML::Writer)
BuildRequires:	perl(YAML) >= 0.39
BuildRequires:	perl(strictures)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Package::Variant)
BuildRequires:	perl(Class::Method::Modifiers)
Requires:	perl(Class::Method::Modifiers)
BuildArch:	noarch

%description
SQL::Translator is a group of Perl modules that converts
vendor-specific SQL table definitions into other formats, such as
other vendor-specific SQL, ER diagrams, documentation (POD and HTML),
XML, and Class::DBI classes. The main focus of SQL::Translator is SQL,
but parsers exist for other structured data formats, including Excel
spreadsheets and arbitrarily delimited text files. Through the
separation of the code into parsers and producers with an object model
in between, it's possible to combine any parser with any producer, to
plug in custom parsers or producers, or to manipulate the parsed data
via the built-in object model. Presently only the definition parts of
SQL are handled (CREATE, ALTER), not the manipulation of data (INSERT,
UPDATE, DELETE).


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
%defattr(0644,root,root,0755)
%doc Changes README
%attr(0755,root,root) %{_bindir}/sqlt*
%{perl_vendorlib}/SQL
%{perl_vendorlib}/Test
%{perl_vendorlib}/auto
%{_mandir}/man*/*
