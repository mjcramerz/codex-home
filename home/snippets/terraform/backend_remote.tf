terraform {
  backend "remote" {
    organization = "example-org"
    workspaces {
      name = "example-workspace"
    }
  }
}
