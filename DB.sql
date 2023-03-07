-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Datawarehouse
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Datawarehouse
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Datawarehouse` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema datawarehouse1
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema datawarehouse
-- -----------------------------------------------------
USE `Datawarehouse` ;

-- -----------------------------------------------------
-- Table `Datawarehouse`.`estados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Datawarehouse`.`estados` (
  `idestados` VARCHAR(5) NOT NULL,
  `nombre` VARCHAR(60) NULL,
  PRIMARY KEY (`idestados`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Datawarehouse`.`ciudades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Datawarehouse`.`ciudades` (
  `idciudades` VARCHAR(5) NOT NULL,
  `nombre` VARCHAR(60) NULL,
  `poblacion` INT NULL,
  `estados_idestados` VARCHAR(5) NULL,
  PRIMARY KEY (`idciudades`),
  INDEX `fk_ciudades_estados_idx` (`estados_idestados` ASC) VISIBLE,
  CONSTRAINT `fk_ciudades_estados`
    FOREIGN KEY (`estados_idestados`)
    REFERENCES `Datawarehouse`.`estados` (`idestados`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Datawarehouse`.`hospitales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Datawarehouse`.`hospitales` (
  `idhospitales` VARCHAR(5) NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `tipo` VARCHAR(45) NULL,
  `ciudades_idciudades` VARCHAR(5) NULL,
  PRIMARY KEY (`idhospitales`),
  INDEX `fk_hospitales_ciudades1_idx` (`ciudades_idciudades` ASC) VISIBLE,
  CONSTRAINT `fk_hospitales_ciudades1`
    FOREIGN KEY (`ciudades_idciudades`)
    REFERENCES `Datawarehouse`.`ciudades` (`idciudades`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Datawarehouse`.`desarrollofisico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Datawarehouse`.`desarrollofisico` (
  `idEtapaVida` VARCHAR(5) NOT NULL,
  `nombre` VARCHAR(60) NULL,
  `edadLimInf` INT NULL,
  `edadLimSup` INT NULL,
  PRIMARY KEY (`idEtapaVida`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Datawarehouse`.`pacientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Datawarehouse`.`pacientes` (
  `idpacientes` VARCHAR(5) NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `edad` INT NULL,
  `sexo` VARCHAR(1) NULL,
  `idCiudad` VARCHAR(5) NULL,
  `desarrollofisico_idEtapaVida` VARCHAR(5) NULL,
  PRIMARY KEY (`idpacientes`),
  INDEX `fk_pacientes_desarrollofisico1_idx` (`desarrollofisico_idEtapaVida` ASC) VISIBLE,
  CONSTRAINT `fk_pacientes_desarrollofisico1`
    FOREIGN KEY (`desarrollofisico_idEtapaVida`)
    REFERENCES `Datawarehouse`.`desarrollofisico` (`idEtapaVida`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Datawarehouse`.`facturas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Datawarehouse`.`facturas` (
  `idfacturas` VARCHAR(5) NOT NULL,
  `fecha` DATE NULL,
  `hora` DATETIME NULL,
  `subtotal` DECIMAL(6,2) NULL,
  `iva` DECIMAL(6,2) NULL,
  `total` DECIMAL(6,2) NULL,
  `hospitales_idhospitales` VARCHAR(5) NULL,
  `pacientes_idpacientes` VARCHAR(5) NULL,
  PRIMARY KEY (`idfacturas`),
  INDEX `fk_facturas_hospitales1_idx` (`hospitales_idhospitales` ASC) VISIBLE,
  INDEX `fk_facturas_pacientes1_idx` (`pacientes_idpacientes` ASC) VISIBLE,
  CONSTRAINT `fk_facturas_hospitales1`
    FOREIGN KEY (`hospitales_idhospitales`)
    REFERENCES `Datawarehouse`.`hospitales` (`idhospitales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturas_pacientes1`
    FOREIGN KEY (`pacientes_idpacientes`)
    REFERENCES `Datawarehouse`.`pacientes` (`idpacientes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Datawarehouse`.`doctores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Datawarehouse`.`doctores` (
  `iddoctores` VARCHAR(5) NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `sueldo` INT NULL,
  `especialidad` VARCHAR(45) NULL,
  `hospitales_idhospitales` VARCHAR(5) NULL,
  PRIMARY KEY (`iddoctores`),
  INDEX `fk_doctores_hospitales1_idx` (`hospitales_idhospitales` ASC) VISIBLE,
  CONSTRAINT `fk_doctores_hospitales1`
    FOREIGN KEY (`hospitales_idhospitales`)
    REFERENCES `Datawarehouse`.`hospitales` (`idhospitales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Datawarehouse`.`conceptos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Datawarehouse`.`conceptos` (
  `idconceptos` VARCHAR(5) NOT NULL,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idconceptos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Datawarehouse`.`factdetalle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Datawarehouse`.`factdetalle` (
  `cant` INT NULL,
  `precioUnit` INT NULL,
  `subtotalConcept` INT NULL,
  `iva` DECIMAL(6,2) NULL,
  `totalCont` DECIMAL(6,2) NULL,
  `doctores_iddoctores` VARCHAR(5) NULL,
  `facturas_idfacturas` VARCHAR(5) NOT NULL,
  `conceptos_idconceptos` VARCHAR(5) NOT NULL,
  INDEX `fk_factdetalle_doctores1_idx` (`doctores_iddoctores` ASC) VISIBLE,
  PRIMARY KEY (`facturas_idfacturas`, `conceptos_idconceptos`),
  INDEX `fk_factdetalle_conceptos1_idx` (`conceptos_idconceptos` ASC) VISIBLE,
  CONSTRAINT `fk_factdetalle_doctores1`
    FOREIGN KEY (`doctores_iddoctores`)
    REFERENCES `Datawarehouse`.`doctores` (`iddoctores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_factdetalle_facturas1`
    FOREIGN KEY (`facturas_idfacturas`)
    REFERENCES `Datawarehouse`.`facturas` (`idfacturas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_factdetalle_conceptos1`
    FOREIGN KEY (`conceptos_idconceptos`)
    REFERENCES `Datawarehouse`.`conceptos` (`idconceptos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;