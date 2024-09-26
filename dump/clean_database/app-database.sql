-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: app-database
-- Tiempo de generación: 26-09-2024 a las 00:19:19
-- Versión del servidor: 5.7.44
-- Versión de PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `app-database`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cards`
--

CREATE TABLE `cards` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `num` int(2) NOT NULL,
  `idDeck` int(11) NOT NULL,
  `board` varchar(255) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `deck`
--

CREATE TABLE `deck` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `idPlayer` int(11) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `league`
--

CREATE TABLE `league` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `player`
--

CREATE TABLE `player` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `position` int(11) NOT NULL,
  `idTournament` int(11) NOT NULL,
  `idDeck` int(11) DEFAULT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tournament`
--

CREATE TABLE `tournament` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `idLeague` int(11) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cards`
--
ALTER TABLE `cards`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `deck`
--
ALTER TABLE `deck`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `league`
--
ALTER TABLE `league`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tournament`
--
ALTER TABLE `tournament`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cards`
--
ALTER TABLE `cards`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `deck`
--
ALTER TABLE `deck`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `league`
--
ALTER TABLE `league`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `player`
--
ALTER TABLE `player`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tournament`
--
ALTER TABLE `tournament`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
