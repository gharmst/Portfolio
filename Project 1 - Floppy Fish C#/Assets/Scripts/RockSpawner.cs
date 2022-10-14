using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RockSpawner : MonoBehaviour
{

    public float maxTime = 1;
    private float timer = 0;
    public GameObject rock;

    // Start is called before the first frame update
    void Start()
    {
        GameObject newRock = Instantiate(rock);
        newRock.transform.position = transform.position + new Vector3(0, Random.Range(-3, 3), 0);
    }

    // Update is called once per frame
    void Update()
    {
        if (timer > maxTime)
        {
            GameObject newRock = Instantiate(rock);
            newRock.transform.position = transform.position + new Vector3(0, Random.Range(-3, 3), 0);
            Destroy(newRock, 7);
            timer = 0;
        }
        timer += Time.deltaTime;
    }
}
