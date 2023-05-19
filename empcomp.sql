-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 13, 2023 at 06:52 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `empcomp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`uname`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `id` int(50) NOT NULL auto_increment,
  `uname` varchar(50) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `ctype` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `details` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `urate` varchar(10) NOT NULL,
  `feed` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`id`, `uname`, `dept`, `ctype`, `location`, `date`, `details`, `image`, `status`, `urate`, `feed`) VALUES
(1, 'pandiyan', 'bca', 'Harassment', 'trichy', '2022-04-14', 'sample', 'download (1).jpg', 'sample', '', ''),
(2, 'k222', 'production', 'Abusing', 'sample', '2022-04-15', 'details', 'Employee-leave-management.jpg', 'sample test', '', ''),
(3, 'kumar123', 'production', 'Harassment', 'trichy', '2022-04-14', 'Harassment', 'yoga.docx', 'solution', '', ''),
(4, 'admin', 'water', 'Facilities', 'trichy', '2023-02-18', 'trichy', 'templatemo_gallery_image_9.jpg', 'sampletest', '2', 'sample');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `qual` varchar(50) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `name`, `gender`, `email`, `phone`, `qual`, `dept`, `address`, `place`, `uname`, `password`) VALUES
(1, 'sundar', 'male', 'sundarv06@gmail.com', '7904461600', 'be', 'cd', 'trichy', 'trichy', '111', '111'),
(2, 'panadiyan', 'male', 'sundarv06@gmail.com', '7904461600', 'be', 'production', 'trichy', 'trichy', 'pandiyan', '123456'),
(3, 'kumar', 'male', 'sundarv06@gmail.com', '7904461600', 'be', 'production', 'trichy', 'trichy', 'k222', 'k222'),
(4, 'sundar', 'male', 'sundarv06@gmail.com', '1231231231', 'be', 'cd', 'trichy', 'trichy', 'admin', '123'),
(5, 'kumar', 'male', 'sundarv@gmail.com', '7904461622', 'be', 'production', 'trichy', 'trichy', 'kumar123', 'k123'),
(6, 'sam', 'male', 'sundarv06@gmail.com', '7904461600', 'test', 'teset', 'trichy', 'trichy', 'admin', 'asdf'),
(7, 'sam', 'male', 'sundarv06@gmail.com', '7904461600', 'test', 'teset', 'trichy', 'trichy', 'admin12', 'admin12');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `gender`, `email`, `phone`, `address`, `place`, `uname`, `password`) VALUES
(7, 'sundar', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', 'trichy', 'admin', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `userfile`
--

CREATE TABLE `userfile` (
  `id` int(10) NOT NULL auto_increment,
  `uname` varchar(10) NOT NULL,
  `date` varchar(10) NOT NULL,
  `details` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `pkey` varchar(100) NOT NULL,
  `b1` varchar(500) NOT NULL,
  `b2` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `userfile`
--

INSERT INTO `userfile` (`id`, `uname`, `date`, `details`, `fname`, `pkey`, `b1`, `b2`) VALUES
(1, 'admin', '2023-01-11', 'test', 'human.sql', '', '', '');
