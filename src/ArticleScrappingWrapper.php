<?php
namespace MehrdadDadkhah\Scrapp;

use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;

/**
 * simple php and python wrapper on hazm persian text processor.
 */
class ArticleScrappingWrapper
{
    public function scrapp(string $url)
    {
        $command = 'python3 ' . dirname(__FILE__) . '/ArticleScrapping.py ' . "'" . $url . "'";

        $process = new Process($command, null, null, null, null);
        $process->run();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }

        return json_decode($process->getOutput(), true);
    }
}
