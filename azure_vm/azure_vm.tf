terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

provider "azurerm" {
  skip_provider_registration = true
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

# Create a public IP address
resource "azurerm_public_ip" "public_ip" {
  name                = "cloud-1-ip-hakahmed"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  allocation_method   = "Static"
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
    public_ip_address_id = azurerm_public_ip.public_ip.id
  }
}


# Create the actual VM itself
resource "azurerm_linux_virtual_machine" "vm" {
  name                  = "cloud-1-vm-hakahmed"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location
  size                  = "Standard_B2s"
  admin_username        = "hakahmed"
  network_interface_ids = [
    azurerm_network_interface.nic.id,
  ]

  admin_ssh_key {
    username   = "hakahmed"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "canonical"
    offer     = "0001-com-ubuntu-server-focal"
    sku       = "20_04-lts"
    version   = "latest"
  }

  disable_password_authentication = true

  tags {
    project = "cloud-1"
  }
}