/*
 * 1D heat conduction problem
 * 
 */

#include <bout.hxx>
#include <boutmain.hxx>
#include <fci_derivs.hxx>

Field3D T;
Vector3D gradT;

BoutReal chi; // Conduction coefficient

int physics_init(bool restarting) {

	// Get the options
	Options *options = Options::getRoot()->getSection("conduction");

	OPTION(options, chi, 1.0); // Read from BOUT.inp, setting default to 1.0

	SOLVE_FOR(T);

	return 0;
}

int physics_run(BoutReal t) {

	mesh->communicate(T); // Communicate guard cells
	ddt(T) = chi*Laplace(T);
	
	return 0;
}
