{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs; [
    python3Full
    git
  ];
  shellHook = ''
    python3 -m venv venv
    venv/bin/python3 -m pip install -r requirements.txt > /dev/null
    source venv/bin/activate
    export PS1="\n\[\033[1;32m\][venv-shell:\w]\$\[\033[0m\] "
  '';
}
