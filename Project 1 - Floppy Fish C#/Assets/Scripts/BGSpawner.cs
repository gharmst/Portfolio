using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BGSpawner : MonoBehaviour
{

    public float maxTime = 1;
    private float timer = 0;
    public GameObject bg;

    // Start is called before the first frame update
    void Start()
    {
        GameObject newBG = Instantiate(bg);
        newBG.transform.position = transform.position + new Vector3(0, 1, 0);
    }

    // Update is called once per frame
    void Update()
    {
        if (timer > maxTime)
        {
            GameObject newBG = Instantiate(bg);
            newBG.transform.position = transform.position + new Vector3(0, 1, 0);
            Destroy(newBG, 7);
            timer = 0;
        }
        timer += Time.deltaTime;
    }
}
