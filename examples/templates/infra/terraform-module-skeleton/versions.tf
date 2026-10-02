terraform {
  required_version = "1.6.0"
  required_providers {
    example = {
      source  = "example/provider"
      version = "1.0.0"
    }
  }
}
