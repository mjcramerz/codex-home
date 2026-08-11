use assert_cmd::Command;

#[test]
fn help_works() {
    let output = Command::cargo_bin("rust_cli_template")
        .unwrap()
        .arg("--help")
        .output()
        .unwrap();
    assert!(output.status.success());
    let stdout = String::from_utf8_lossy(&output.stdout);
    assert!(stdout.contains("--log-format"));
}

#[test]
fn version_works() {
    Command::cargo_bin("rust_cli_template")
        .unwrap()
        .arg("--version")
        .assert()
        .success();
}
