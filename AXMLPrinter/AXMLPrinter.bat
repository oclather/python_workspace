:AXMLprinter
@set /p filepath=������Ҫ���ܵ�XML�ļ�:

@echo off

set new_xml=%filepath:AndroidManifest.xml=Manifest.txt%  

java -jar AXMLPrinter2.jar  %filepath% > %new_xml%

%new_xml%
@echo XML�ļ����ܳɹ���
@goto :AXMLprinter

