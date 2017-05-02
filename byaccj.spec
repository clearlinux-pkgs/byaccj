Name     : byaccj
Version  : 1.15_src
Release  : 3
URL      : http://sourceforge.net/projects/byaccj/files/byaccj/1.15/byaccj1.15_src.tar.gz
Source0  : http://sourceforge.net/projects/byaccj/files/byaccj/1.15/byaccj1.15_src.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain

%description
1.  The documentation for this code is found at:
http://byaccj.sourceforge.net
It is also in the ./doc directory.

%prep
%setup -q -n byaccj1.15
sed -i -e 's|-arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -mmacosx-version-min=10.4||g' src/Makefile

%build
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
pushd src
make linux 
popd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp -p src/yacc.linux %{buildroot}/usr/bin/byaccj

# Documentation
mkdir -p %{buildroot}/usr/share/doc/byaccj
cp docs/* src/README %{buildroot}/usr/share/doc/byaccj

%files
%defattr(-,root,root,-)
/usr/bin/byaccj
/usr/share/doc/byaccj/ACKNOWLEDGEMEN
/usr/share/doc/byaccj/README
/usr/share/doc/byaccj/tf.y
/usr/share/doc/byaccj/yacc.cat
