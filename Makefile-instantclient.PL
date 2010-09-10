#
# Script:   Makefile-instantclient.PL
#
# Subject:  DBD-Oracle module compilation from Instantclient only installation 
# Author:   Jean-Christophe Duberga - CRI - Bordeaux 2 University
# Contact:  jeanchristophe.duber@free.fr
#
# WARNINBG: this script have only been tested under linux and should only
#           work on unix like systems

use ExtUtils::MakeMaker;
use Getopt::Long;
use Config;
use Cwd;
use File::Find;
use strict;
use DBI 1.28;
use DBI::DBD;

# Get infos given by oracle-instantclient-config

my $version = `oracle-instantclient-config --version`
  or die "oracle-instantclient-config not found ( in PATH ) !\n"
        ."Please check, your installation of Oracle InstantClient\n"
	."You need InstantClient Basic+SDK and the oracle-instantclient script\n";	
my $cflags  = `oracle-instantclient-config --cflags`;
my $libs    = `oracle-instantclient-config --libs`;

chomp( $version);
chomp( $cflags);
chomp( $libs);

my $dbi_arch_dir = dbd_dbi_arch_dir();

# Define attributes needed for Makefile generation

my %opts = (
    NAME => 'DBD::Oracle',
    AUTHOR => 'Tim Bunce (dbi-users@perl.org)',    
    VERSION_FROM => 'Oracle.pm',
    PREREQ_PM => { "DBI" => 0 },
    EXE_FILES => [ "ora_explain" ],
    OBJECT => '$(O_FILES)',
    DEFINE => '',
    CCFLAGS => '',
    INC => '',
    LIBS => '',
    DIR  => [],
    clean => {	FILES	=> 'xstmp.c Oracle.xsi dll.base dll.exp sqlnet.log libOracle.def ora_explain mk.pm' },
    dist  => {
	DIST_DEFAULT	=> 'clean distcheck disttest tardist',
	PREOP		=> '$(MAKE) -f Makefile.old distdir',
	COMPRESS	=> 'gzip -v9', SUFFIX => 'gz',
    },
);

$opts{DEFINE} = ' -Wall -Wcast-align -Wpointer-arith -DORA_OCI_VERSION=\"'.$version.'\"';

$opts{INC} = "-I$dbi_arch_dir";

$opts{CCFLAGS} = $cflags;

$opts{LIBS} = $libs;

# Now, write the makefile 

WriteMakefile( %opts );

sub MY::postamble {
    main::dbd_postamble(@_);
}
	
