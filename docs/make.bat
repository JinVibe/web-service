@echo off
setlocal

pushd %~dp0

set SOURCEDIR=source
set BUILDDIR=build

if "%1"=="" (
  echo Usage: make.bat ^<target^>   e.g. make.bat html
  set SPHINXBUILD=sphinx-build
  %SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR%
  popd
  exit /b 0
)

set SPHINXBUILD=sphinx-build
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

popd
endlocal
