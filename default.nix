{ buildPythonPackage
, pip
, setuptools
, pkgs ? import <nixpkgs> {}
, g4f ? (pkgs.python3Packages.callPackage /home/diratof/Documents/g4f-nix/default.nix {})
}:
buildPythonPackage rec {
  name = "gpt_is";
  src = /home/diratof/Documents/llm_audit;
  nativeBuildInputs = [ 
    pip
    setuptools
    g4f
  ];
  doCheck = false;
}
