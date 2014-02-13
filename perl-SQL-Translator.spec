%define upstream_name	 SQL-Translator
%define upstream_version 0.11018

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Doesnt(.*)\\)|perl\\(GD(.*)\\)|perl\\(GraphViz(.*)\\)|perl\\(IO::File(.*)\\)|perl\\(IO::Scalar(.*)\\)|perl\\(Spreadsheet::ParseExcel(.*)\\)|perl\\(Template(.*)\\)|perl\\(Text::ParseWords(.*)\\)|perl\\(Text::RecordParser(.*)\\)|perl\\(XML::Writer(.*)\\)|perl\\(XML::XPath(.*)\\)'
%else
%define _requires_exceptions perl(Doesnt\\|perl(GD\\|perl(GraphViz\\|perl(IO::File\\|perl(IO::Scalar\\|perl(Spreadsheet::ParseExcel\\|perl(Template\\|perl(Text::ParseWords\\|perl(Text::RecordParser\\|perl(XML::Writer\\|perl(XML::XPath
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Manipulate structured data definitions (SQL and more)
License:	GPL
Group:		Development/Perl
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/SQL/SQL-Translator-%{upstream_version}.tar.gz
Url:		http://search.cpan.org/dist/%{upstream_name}

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
%doc AUTHORS Changes LICENSE README
%attr(0755,root,root) %{_bindir}/sqlt*
%{perl_vendorlib}/SQL
%{perl_vendorlib}/Test
%{perl_vendorlib}/auto
%{_mandir}/man*/*



%changelog
* Sat Jun 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.80-1mdv2011.0
+ Revision: 687100
- new version

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.70-1mdv2011.0
+ Revision: 612255
- update to new version 0.11007

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.60-1mdv2011.0
+ Revision: 553155
- update to 0.11006

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.50-1mdv2010.1
+ Revision: 510977
- update to 0.11005

* Mon Feb 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.40-1mdv2010.1
+ Revision: 506244
- update to 0.11004

* Tue Sep 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.30-1mdv2010.0
+ Revision: 450783
- update to 0.11003

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.20-1mdv2010.0
+ Revision: 422799
- update to 0.11002
- update to 0.11001

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.10-1mdv2010.0
+ Revision: 418118
- update to 0.11001

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 417017
- adding missing buildrequires:
- update to 0.10

* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.70-1mdv2010.0
+ Revision: 393269
- adding missing buildrequires:
- forgot to replace a version
- update to 0.09007
- using %%perl_convert_version

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.08.01-3mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08.01-3mdv2008.0
+ Revision: 86872
- rebuild


* Mon Aug 07 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-07 19:31:23 (54064)
- Added _requires_exceptions to work around bug #24193 and to account for "recommends."

* Mon Aug 07 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-07 13:53:18 (53881)
- import perl-SQL-Translator-0.08.01-1mdv2007.0

* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org> 0.08.01-1mdv2007.0
- First Mandriva package


