terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

provider "azurerm" {
  skip_provider_registration = true # This is only required when the User, Service Principal, or Identity running Terraform lacks the permissions to register Azure Resource Providers.
  features {}
}

# Resource group for the VM
resource "azurerm_resource_group" "rg" {
  name     = "cloud-1-hakahmed"
  location = "West Europe"
}

# Create a virtual network for the VM
resource "azurerm_virtual_network" "vnet" {
  name                = "cloud-1-vnet-hakahmed"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# Create a subnet fo the VNet
resource "azurerm_subnet" "subnet" {
  name                 = "cloud-1-subnet-hakahmed"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.2.0/24"]
}

# Create a Network Interface Card
resource "azurerm_network_interface" "nic" {
  name                = "cloud-1-nic-hakahmed"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
  }
}

