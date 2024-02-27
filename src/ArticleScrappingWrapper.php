<?php
namespace MehrdadDadkhah\Scrapp;

use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;

/**
 * PHP wrapper for python newspaper3k text processor.
 */
class ArticleScrappingWrapper
{
    /**
     * Accepts url string and returns Article object as an associative array.
     * 
     * @param string $url
     * 
     * @return array|object
     */
    public function scrapp(string $url)
    {
        $command = 'python3';
        $executable = dirname(__FILE__) . '/ArticleScrapping.py';

        $commands = [$command, $executable, $url];

        $process = new Process($commands, null, null, null, null);
        $process->run();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }

        return json_decode($process->getOutput(), true);
    }
}
