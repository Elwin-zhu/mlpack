librule(
	name="fock_matrix",
	headers=[],
	sources=[],
	deplibs=["fastlib:fastlib"],
	tests=[]
)

librule(
	name="eri",
	headers=["eri.h", "shell_pair.h", "basis_shell.h", "basis_function.h"],
	sources=["eri.cc"],
	deplibs=["fastlib:fastlib"]
)

librule(
	name="schwartz_prescreening",
	headers=["schwartz_prescreening.h"],
	sources=["schwartz_prescreening.cc"],
	deplibs=["fastlib:fastlib", ":eri"],
	tests=[]
)

binrule(
	name="schwartz_prescreening_main",
	sources=["schwartz_prescreening_main.cc"],
	deplibs=["fastlib:fastlib", ":schwartz_prescreening", ":eri"]
)