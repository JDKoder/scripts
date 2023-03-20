#!/bin/bash

#2 branches
#assumes both branches are updated
#specify file type eg. *

function findAllOfType() {
    grep --include=\*${1} --exclude=\*.dbranches -rlU '.'
}

function getBranch() {
    git checkout ${1}
}

function stashChanges() {
    git stash
}

function popChanges() {
    git stash pop
}

function updateBranch() {
    git pull -r
}

function contextDiff() {
    diff -U 0 $1 $2
}

function currentBranch() {
    git rev-parse --abbrev-ref HEAD
}

function dbranches() {
    #TODO: check arguments before running program args as follows
    #$1 first branch
    #$2 second branch
    #$3 filename

    cbranch=$(currentBranch > /dev/null 2>&1; echo $?)
    stashChanges > /dev/null
    getBranch $1
    updateBranch
    findAllOfType $3 > 1.dbranches
    getBranch $2
    updateBranch
    findAllOfType $3 > 2.dbranches
    getBranch ${cbranch}
    popChanges > /dev/null
    contextDiff 1.dbranches 2.dbranches
}
