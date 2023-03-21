#!/bin/bash

#2 branches
#assumes both branches are updated
#specify file type eg. *

#This will find all files recursively beneath the current directory that match the name given as 
#the first input.
#Explicitly skips the contents of .git, node_modules, and target directories.
#Explicitly skips .dbranches files.
function findAllFiles() {
    find . -name "*${1}" \
        ! -name "*.dbranches" \
        -not -path "*/.git/*" \
        -not -path "*/node_modules/*" \
        -not -path "*/target/*"
}

#deprecated because this skips empty files.  ALL files that are not explicitly excluded should be found. 
function findAllOfType() {
    grep --include=\*${1} --exclude=\*.dbranches -rl '.'
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

function dbranchCleanup() {
    rm -v *.dbranches
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
    findAllFiles $3 > 1.dbranches
    getBranch $2
    updateBranch
    findAllFiles $3 > 2.dbranches
    getBranch ${cbranch}
    popChanges > /dev/null
    contextDiff 1.dbranches 2.dbranches
}
