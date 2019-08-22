-- all the data I input and used in my video 

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO"; -- 
SET AUTOCOMMIT = 0;  --since in my sql autocommit is on by default, i am turning it of and starting transaction
START TRANSACTION;

-- --------------------------------------------------------

--
-- Table structure for table `coaches`
--

CREATE TABLE `coaches` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `coaches`
--

INSERT INTO `coaches` (`id`, `first_name`, `last_name`, `email`) VALUES
(1, 'Gregg', 'Berhalter', 'greg@gmail.com'),
(2, 'Ben', 'Olsen', 'ben@gmail.com'),
(3, 'Mauro', 'Biello', 'Biello@gmail.com'),
(4, 'Jay', 'Heaps', 'Heaps@gmail.com'),
(5, 'Patrick', 'Vieira', 'Vieira@gmail.com'),
(6, 'Jesse', 'Marsch', 'Marsch@gmail.com'),
(7, 'Jason', 'Kreis', 'Kreis@gmail.com'),
(8, 'Pablo', 'Mastroeni', 'Mastroeni@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `matches`
--

CREATE TABLE `matches` (
  `id` int(11) NOT NULL,
  `team_1_id` int(11) NOT NULL,
  `team_2_id` int(11) NOT NULL,
  `team_1_score` int(11) NOT NULL,
  `team_2_score` int(11) NOT NULL,
  `location` varchar(60) NOT NULL,
  `date` date NOT NULL,
  `winner` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `matches`
--

INSERT INTO `matches` (`id`, `team_1_id`, `team_2_id`, `team_1_score`, `team_2_score`, `location`, `date`, `winner`) VALUES
(1, 3, 5, 1, 5, 'Los Angeles', '2018-12-12', 5),
(2, 4, 5, 0, 0, 'Merced', '2018-12-19', 0),
(3, 4, 3, 6, 3, 'Los Angeles', '2018-12-11', 4),
(4, 7, 6, 4, 3, 'Los Angeles', '2018-12-12', 7),
(5, 8, 4, 0, 0, 'Denver', '2018-12-20', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `players`
--

CREATE TABLE `players` (
  `id` int(11) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(60) NOT NULL,
  `town` varchar(60) NOT NULL,
  `team_id` int(11) NOT NULL,
  `position` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `players`
--

INSERT INTO `players` (`id`, `first_name`, `last_name`, `email`, `town`, `team_id`, `position`) VALUES
(1, 'Taylor', 'Kemp', 'Taylorkemp@gmail.com', 'batesville', 3, 'defender'),
(2, 'Dilly', 'Duka', 'Dillyduka@gmail.com', 'arkansas post', 3, 'midfielder'),
(3, 'Tony', 'Tchani', 'tony@gmail.com', 'Hope', 3, 'midfielder'),
(4, 'Sean', 'Franklin', 'Seanfranklin@gmail.com', 'Alameda', 4, 'defender'),
(5, 'Kofi', 'Opare', 'Kofiopare@gmail.com', 'Eureka', 4, 'defender'),
(6, 'Chris', 'Rolfe', 'Rolfe@gmail.com', 'Indio', 4, 'Forward'),
(7, 'Ola', 'Kamara', 'Olakamara@gmail.com', 'Lodi', 3, 'Forward'),
(8, 'Zack', 'Steffen', 'Steffen@gmail.com', 'Napa', 3, 'Goalkeeper'),
(9, 'Alhaji', 'Kamara', 'Alhajikamara@gmail.com', 'Novato', 4, 'Forward');

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE `teams` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `logo_url` varchar(500) NOT NULL,
  `coach_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`id`, `name`, `email`, `city`, `state`, `logo_url`, `coach_id`) VALUES
(3, 'Columbus CSC', 'ColumbusCSC@gmail.com', 'Columbus', 'Ohio', 'https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/I/m/Columbus_Crew_SC_Logo.svg.png', 1),
(4, 'D.C. United', 'DCUnited@gmail.com', 'Washington, D.C', 'Washington', 'https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/I/m/D.C._United_logo_(2016).svg.png', 2),
(5, 'New England Revolution', 'Newer@gmail.com', 'Boston', 'Massachusetts', 'https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/I/m/New_England_Revolution_logo.svg.png', 4),
(6, 'New York City FC', 'NewYCFC@gmail.com', 'New York', 'New York', 'https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/I/m/New_York_City_FC.svg.png', 5),
(7, 'New York Red Bulls', 'nyrb@gmail.com', 'New York', 'New York', 'https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/I/m/New_York_Red_Bulls_logo.svg.png', 6),
(8, 'Colorado Rapids', 'Coloradorapids@gmail.com', 'Denver', 'Colorado', 'https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/I/m/Colorado_Rapids_logo.svg.png', 8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `coaches`
--
ALTER TABLE `coaches`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `matches`
--
ALTER TABLE `matches`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `players`
--
ALTER TABLE `players`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teams`
--
ALTER TABLE `teams`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `coaches`
--
ALTER TABLE `coaches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `matches`
--
ALTER TABLE `matches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `players`
--
ALTER TABLE `players`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `teams`
--
ALTER TABLE `teams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
-19', 0),
(3, 4, 3, 6, 3, 'Los Angeles', '2018-12-11', 4),
(4, 7, 6, 4, 3, 'Los Angeles', '2018-12-12', 7),
(5, 8, 4, 0, 0, 'Denver', '2018-12-20', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `players`
--

CREATE TABLE `players` (
  `id` int(11) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(60) NOT NULL,
  `town` varchar(60) NOT NULL,
  `team_id` int(11) NOT NULL,
  `position` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `players`
--

INSERT INTO `players` (`id`, `first_name`, `last_name`, `email`, `town`, `team_id`, `position`) VALUES
(1, 'Taylor', 'Kemp', 'Taylorkemp@gmail.com', 'batesville', 3, 'defender'),
(2, 'Dilly', 'Duka', 'Dillyduka@gmail.com', 'arkansas post', 3, 'midfielder'),
(3, 'Tony', 'Tchani', 'tony@gmail.com', 'Hope', 3, 'midfielder'),
(4, 'Sean', 'Franklin', 'Seanfranklin@gmail.com', 'Alameda', 4, 'defender'),
(5, 'Kofi', 'Opare', 'Kofiopare@gmail.com', 'Eureka', 4, 'defender'),
(6, 'Chris', 'Rolfe', 'Rolfe@gmail.com', 'Indio', 4, 'Forward'),
(7, 'Ola', 'Kamara', 'Olakamara@gmail.com', 'Lodi', 3, 'Forward'),
(8, 'Zack', 'Steffen', 'Steffen@gmail.com', 'Napa', 3, 'Goalkeeper'),
(9, 'Alhaji', 'Kamara', 'Alhajikamara@gmail.com', 'Novato', 4, 'Forward');

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE `teams` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `logo_url` varchar(500) NOT NULL,
  `coach_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`id`, `name`, `email`, `city`, `state`, `logo_url`, `coach_id`) VALUES
(3, 'Columbus CSC', 'ColumbusCSC@gmail.com', 'Columbus', 'Ohio', 'https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/I/m/Columbus_Crew_SC_Logo.svg.png', 1),
(4, 'D.C. United', 'DCUnited@gmail.com', 'Washi