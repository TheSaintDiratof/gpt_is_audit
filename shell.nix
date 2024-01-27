{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs; let 
    g4f = python3Packages.callPackage ./llm_audit.pkgs/g4f-nix/default.nix {};
    llm_audit = python3Packages.callPackage ./llm_audit.pkgs/llm_audit.nix {g4f = g4f;};
  in [
    python3Full
    git
    vim
    nodejs vscode
    llm_audit
  ];
  shellHook = ''
    export PS1="\n\[\033[1;32m\][venv-shell:\w]\$\[\033[0m\] "
  '';
}
