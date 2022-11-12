Name:		texlive-harpoon
Version:	21327
Release:	1
Summary:	Extra harpoons, using the graphics package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/harpoon
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harpoon.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harpoon.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides over- and under-harpoon symbol commands; the harpoons
may point in either direction, with the hook pointing up or
down. The covered object is provided as an argument to the
commands, so that they have the look of accent commands.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/harpoon/harpoon.sty
%doc %{_texmfdistdir}/doc/latex/harpoon/harpoon.pdf
%doc %{_texmfdistdir}/doc/latex/harpoon/harpoon.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
