variable "IMAGE_NAME" {
  default = "app"
}

group "default" {
  targets = ["runtime"]
}

target "runtime" {
  dockerfile = "Dockerfile"
  tags = ["${IMAGE_NAME}:local"]
  platforms = ["linux/amd64"]
}
