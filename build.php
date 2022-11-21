<?php

	$txt = " appended php " . gmdate("Y-m-d H:i:s") . " (random string " . substr(md5(rand()), 0, 7) . ")";

	$myfile = file_put_contents('README.md', PHP_EOL.'- '.$txt , FILE_APPEND | LOCK_EX);
