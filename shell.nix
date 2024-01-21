{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs; [
    python3Full
    git
    vim
    nodejs vscode
    (python3Packages.callPackage /home/diratof/Documents/g4f-nix/default.nix {})
    (python3Packages.callPackage /home/diratof/Documents/gpt_is/default.nix {})
  ];
  shellHook = ''
    export PS1="\n\[\033[1;32m\][venv-shell:\w]\$\[\033[0m\] "
  '';
}
