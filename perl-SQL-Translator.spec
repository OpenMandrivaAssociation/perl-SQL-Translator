%define module	SQL-Translator
%define name	perl-%{module}
%define	modprefix SQL

%define realversion 0.08_01
%define version 0.08.01

%define	rel	2
%define release %mkrel %{rel}

%define _requires_exceptions perl(Doesnt\\|perl(GD\\|perl(GraphViz\\|perl(IO::File\\|perl(IO::Scalar\\|perl(Spreadsheet::ParseExcel\\|perl(Template\\|perl(Text::ParseWords\\|perl(Text::RecordParser\\|perl(XML::Writer\\|perl(XML::XPath

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Summary:	Manipulate structured data definitions (SQL and more)
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{realversion}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Class::Base)
BuildRequires:	perl(Class::Data::Inheritable) >= 0.02
BuildRequires:	perl(Class::MakeMethods)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Dir)
BuildRequires:	perl(Log::Log4perl)
BuildRequires:  perl(Module::Build)
BuildRequires:	perl(Parse::RecDescent) >= 1.94
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More) >= 0.6
BuildRequires:	perl(YAML) >= 0.39
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%setup -q -n %{module}-%{realversion}

%build
%{__perl} Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
## scottk: test disabled until either Template::Toolkit or tests
## 18, 33 and 34 are fixed
##./Build test

%install
rm -rf %{buildroot}
./Build install

%clean 
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS Changes LICENSE README
%attr(0755,root,root) %{_bindir}/sqlt*
%{perl_vendorlib}/%{modprefix}
%{perl_vendorlib}/Test
%{_mandir}/man*/*



