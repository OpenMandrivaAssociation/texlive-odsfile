# revision 32742
# category Package
# catalog-ctan /macros/luatex/latex/odsfile
# catalog-date 2012-08-14 16:24:07 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-odsfile
Version:	0.2
Release:	8
Summary:	Read OpenDocument Spreadsheet documents as LaTeX tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/odsfile
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/odsfile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/odsfile.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The distribution includes a package and a lua library that can
together read OpenDocument spreadsheet documents as LaTeX
tables. Cells in the tables may be processed by LaTeX macros,
so that (for example) the package may be used for drawing some
plots. The package uses lua's zip library.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/odsfile/odsfile.lua
%{_texmfdistdir}/tex/lualatex/odsfile/odsfile.sty
%doc %{_texmfdistdir}/doc/lualatex/odsfile/README
%doc %{_texmfdistdir}/doc/lualatex/odsfile/odsfile.pdf
%doc %{_texmfdistdir}/doc/lualatex/odsfile/odsfile.tex
%doc %{_texmfdistdir}/doc/lualatex/odsfile/pokus.ods

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
