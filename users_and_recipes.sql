-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema users_and_recipes
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema users_and_recipes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `users_and_recipes` DEFAULT CHARACTER SET utf8 ;
USE `users_and_recipes` ;

-- -----------------------------------------------------
-- Table `users_and_recipes`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users_and_recipes`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `users_and_recipes`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users_and_recipes`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `recipe_name` VARCHAR(45) NULL,
  `recipe_instructions` VARCHAR(45) NULL,
  `users_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `users_and_recipes`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
