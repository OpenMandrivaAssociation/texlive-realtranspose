Name:		texlive-realtranspose
Version:	56623
Release:	2
Summary:	The "real" way to transpose a Matrix
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/realtranspose
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realtranspose.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realtranspose.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realtranspose.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With realtranspose you can notate the transposition of a matrix
by rotating the symbols 90 degrees. This is a hommage to the
realhats package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/realtranspose
%{_texmfdistdir}/tex/latex/realtranspose
%doc %{_texmfdistdir}/doc/latex/realtranspose

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
