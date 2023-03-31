Name:		texlive-odsfile
Version:	65268
Release:	2
Summary:	Read OpenDocument Spreadsheet documents as LaTeX tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/odsfile
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/odsfile.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/odsfile.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
